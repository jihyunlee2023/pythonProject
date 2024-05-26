// app/page.tsx
'use client';

import { useEffect, useState } from 'react'; // useState와 useEffect를 import합니다.
import { TableHead, TableRow, TableHeader, TableCell, TableBody, Table } from "@/components/ui/table";
import { Member } from '../app/types/types';
import Layout from './layout';
import { useRouter } from 'next/router';

const MemberTableRow = ({ name, party, district, attendance }: Member) => {
    const router = useRouter();

  const handleClick = () => {
    router.push('/member');
  };

  return (
    <TableRow className="cursor-pointer hover:bg-gray-100" onClick={handleClick}>
      <TableCell className="font-medium">{name}</TableCell>
      <TableCell>{party}</TableCell>
      <TableCell>{district}</TableCell>
      <TableCell className="text-right">
        <div className="flex items-center justify-end">
          <div className="w-[600%] h-4 bg-gray-200 rounded-full dark:bg-gray-800">
            <div
              className="h-full bg-blue-500 rounded-full"
              style={{
                width: attendance,
              }}
            />
          </div>
          <span className="ml-2">{attendance}</span>
        </div>
      </TableCell>
    </TableRow>
  );
};

export default function Home() {
  // 여기서 상태와 효과 훅을 선언합니다.
  const [user, setUser] = useState(null); // useState 훅을 사용하여 user 상태를 선언합니다.
  const [loading, setLoading] = useState(true); // 로딩 상태 추가

  useEffect(() => {
    fetch('http://127.0.0.1:8002/user')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setUser(data);
        setLoading(false); // 데이터 로딩 완료
      })
      .catch(error => {
        console.error('Error fetching user:', error);
        setLoading(false); // 에러 발생 시에도 로딩 상태를 false로 설정
      });
  }, []);

  // 데이터를 불러오는 동안 로딩 메시지를 표시합니다.
  if (!user) return <div>Loading...</div>;
  if (!user) return <div>No user data</div>; // 데이터가 없는 경우 처리

  // 데이터를 성공적으로 불러온 후에는 사용자 정보를 표시합니다.
  return (
    <Layout>
      <div className="flex-1 overflow-auto">
        <div className="container mx-auto px-24 grid gap-6 py-10">
          <div className="border rounded-lg shadow-sm p-6 w-full">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead className="w-[150px]">이름</TableHead>
                  <TableHead className="w/[100px]">정당</TableHead>
                  <TableHead className="w/[150px]">선거구</TableHead>
                  <TableHead className="text-right">출석률</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {/* API에서 받은 데이터를 사용하여 사용자 정보를 표시합니다. */}
                <MemberTableRow name={user.name} party="더불어민주당" district="서울 해운대구" attendance={92} />
              </TableBody>
            </Table>
          </div>
        </div>
      </div>
    </Layout>
  );
}
