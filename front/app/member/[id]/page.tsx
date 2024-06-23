"use client";

import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';

const MemberDetails = () => {
  const router = useRouter();
  const { id } = router.query;
  const [member, setMember] = useState(null);

  useEffect(() => {
    if (id) {
      const fetchMemberData = async () => {
        try {
          const res = await fetch(`/api/members/${id}`);
          if (!res.ok) {
            throw new Error('Network response was not ok');
          }
          const data = await res.json();
          setMember(data);
        } catch (error) {
          console.error('Error fetching member data:', error);
        }
      };

      fetchMemberData();
    }
  }, [id]);

  if (!member) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{member.name}</h1>
      <p>Party: {member.party}</p>
      <p>Constituency: {member.constituency}</p>
      <p>Terms: {member.terms}</p>
    </div>
  );
};

export default MemberDetails;