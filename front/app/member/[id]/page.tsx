//app/member/[id]/page.tsx

"use client";

import { useParams } from 'next/navigation';
import { useEffect, useState } from 'react';

const MemberDetailPage = () => {
  const { id } = useParams();
  const [memberData, setMemberData] = useState(null);

  useEffect(() => {
    const fetchMemberData = async () => {
      try {
        const response = await fetch(`/api/members/${id}`);
        const data = await response.json();
        setMemberData(data);
      } catch (error) {
        console.error('Error fetching member data:', error);
      }
    };

    if (id) {
      fetchMemberData();
    }
  }, [id]);

  if (!memberData) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{memberData.name}</h1>
      <p>Party: {memberData.party}</p>
      <p>Constituency: {memberData.constituency}</p>
      <p>Gender: {memberData.gender}</p>
      <p>Term: {memberData.term}</p>
      {/* 다른 정보도 여기에 추가 가능 */}
    </div>
  );
};

export default MemberDetailPage;