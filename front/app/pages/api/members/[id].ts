// pages/api/members/[id].ts
import { NextApiRequest, NextApiResponse } from 'next';
import membersData from '@/public/data/members.json'; // JSON 파일의 경로를 확인하세요.

const getMemberById = (id: number) => {
  return membersData.find((member) => member.id === id);
};

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const { id } = req.query;
  const member = getMemberById(Number(id));

  if (member) {
    res.status(200).json(member);
  } else {
    res.status(404).json({ message: 'Member not found' });
  }
}