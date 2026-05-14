#!/usr/bin/env python3
"""Grade a structured JSON submission using an OpenAI model and a rubric.

Usage:
  python grade_submission.py \
    --submission-json submission.json \
    --rubric-path rubric.md \
    --question "Question 1" \
    --student-id "S12345"
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from openai import OpenAI


def load_dotenv(dotenv_path: Path = Path('.env')) -> None:
    if not dotenv_path.exists():
        return
    for raw_line in dotenv_path.read_text(encoding='utf-8').splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description='Grade JSON submission with a rubric.')
    p.add_argument('--submission-json', required=True, help='Path to student submission JSON file.')
    p.add_argument('--rubric-path', required=True, help='Path to rubric text/markdown file.')
    p.add_argument('--question', default='', help='Optional question/prompt identifier.')
    p.add_argument('--student-id', default='', help='Optional student identifier.')
    p.add_argument('--model', default='gpt-4.1', help='OpenAI model for rubric-based grading.')
    return p.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()

    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise SystemExit('OPENAI_API_KEY not found. Put it in .env or environment variables.')

    submission_path = Path(args.submission_json)
    rubric_path = Path(args.rubric_path)

    if not submission_path.exists():
        raise SystemExit(f'Submission JSON not found: {submission_path}')
    if not rubric_path.exists():
        raise SystemExit(f'Rubric file not found: {rubric_path}')

    rubric_text = rubric_path.read_text(encoding='utf-8')

    try:
        submission_obj = json.loads(submission_path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        raise SystemExit(f'Invalid submission JSON: {exc}') from exc

    submission_text = json.dumps(submission_obj, ensure_ascii=False, indent=2)

    client = OpenAI(api_key=api_key)

    prompt = (
        'You are an experienced assessor. Analyze the structured student submission JSON and grade it strictly '
        'against the rubric. Return only valid JSON with this exact schema:\n'
        '{\n'
        '  "student_id": string,\n'
        '  "question": string,\n'
        '  "criterion_scores": [\n'
        '    {"criterion": string, "max_score": number, "awarded_score": number, "justification": string}\n'
        '  ],\n'
        '  "total_score": number,\n'
        '  "max_total": number,\n'
        '  "feedback_summary": string,\n'
        '  "improvement_recommendations": [string],\n'
        '  "confidence": "low" | "medium" | "high"\n'
        '}\n\n'
        'Rules:\n'
        '1) Use only the provided submission JSON and rubric text.\n'
        '2) If evidence is missing/ambiguous, explain uncertainty and lower confidence.\n'
        '3) Be concise and specific in feedback.\n'
    )

    response = client.responses.create(
        model=args.model,
        input=[
            {
                'role': 'user',
                'content': [
                    {'type': 'input_text', 'text': prompt},
                    {'type': 'input_text', 'text': f'Student ID: {args.student_id or "unknown"}'},
                    {'type': 'input_text', 'text': f'Question: {args.question or "unspecified"}'},
                    {'type': 'input_text', 'text': f'Rubric:\n{rubric_text}'},
                    {'type': 'input_text', 'text': f'Submission JSON:\n{submission_text}'},
                ],
            }
        ],
    )

    text = response.output_text.strip()

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        print('Model did not return strict JSON. Raw output:\n')
        print(text)
        raise SystemExit(1)

    print(json.dumps(parsed, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
