'use client';

import { CollapsibleTrigger, CollapsibleContent, Collapsible } from "@/components/ui/collapsible";
import Link from "next/link";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { useRouter } from 'next/navigation';
import { DropdownMenuTrigger, DropdownMenuRadioItem, DropdownMenuRadioGroup, DropdownMenuContent, DropdownMenu } from "@/components/ui/dropdown-menu";
import { TableHead, TableRow, TableHeader, TableCell, TableBody, Table } from "@/components/ui/table";

const MemberTableRow = ({ name, party, district, attendance }) => {
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

export default function Component() {
  return (
    <>
      <header className="flex items-center h-16 px-6 border-b shrink-0 bg-gray-950 dark:bg-gray-950">
        <Collapsible className="flex items-center gap-4">
          <CollapsibleTrigger className="flex items-center gap-2 text-lg font-semibold [&[data-state=open]>svg]:rotate-90]">
            <MenuIcon className="w-6 h-6" />
            <span className="text-gray-50">Menu</span>
            <ChevronDownIcon className="w-4 h-4 ml-auto text-gray-400" />
          </CollapsibleTrigger>
          <CollapsibleContent className="absolute top-16 left-0 z-10 w-full bg-gray-950 border-t border-gray-800 shadow-lg">
            <div className="grid gap-4 p-6">
              <Link className="flex items-center gap-2 text-gray-50 hover:bg-gray-800 px-4 py-2 rounded-md" href="#">
                <PartyPopperIcon className="w-5 h-5" />
                <span>By Party</span>
              </Link>
              <Link className="flex items-center gap-2 text-gray-50 hover:bg-gray-800 px-4 py-2 rounded-md" href="#">
                <LocateIcon className="w-5 h-5" />
                <span>By District</span>
              </Link>
              <Link className="flex items-center gap-2 text-gray-50 hover:bg-gray-800 px-4 py-2 rounded-md" href="#">
                <StarIcon className="w-5 h-5" />
                <span>Favorites</span>
              </Link>
            </div>
          </CollapsibleContent>
        </Collapsible>
        <Link className="flex items-center gap-2 text-lg font-semibold" href="#">
          <MountainIcon className="w-6 h-6" />
          <span className="text-3xl font-bold text-gray-50">국회의원 출석률</span>
        </Link>
        <form className="flex-1">
          <div className="relative">
            <SearchIcon className="absolute left-2.5 top-2.5 h-4 w-4 text-gray-400" />
            <Input
              className="pl-8 sm:w-[300px] md:w-[200px] lg:w/[300px] bg-gray-800 text-gray-50 placeholder:text-gray-400"
              placeholder="의원 검색"
              type="search"
            />
          </div>
        </form>
        <div className="flex gap-2">
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button className="shrink-0 bg-gray-800 text-gray-50 hover:bg-gray-700" variant="outline">
                <ArrowUpDownIcon className="w-4 h-4 mr-2" />
                정렬
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" className="w-[200px] bg-gray-800 text-gray-50">
              <DropdownMenuRadioGroup value="attendance">
                <DropdownMenuRadioItem value="attendance">출석률 높은 순</DropdownMenuRadioItem>
                <DropdownMenuRadioItem value="name">이름 순</DropdownMenuRadioItem>
                <DropdownMenuRadioItem value="party">정당 순</DropdownMenuRadioItem>
                <DropdownMenuRadioItem value="district">지역구 순</DropdownMenuRadioItem>
              </DropdownMenuRadioGroup>
            </DropdownMenuContent>
          </DropdownMenu>
          <Link href="/login">
            <Button className="bg-gray-800 text-gray-50 hover:bg-gray-700" variant="outline">
              로그인
            </Button>
          </Link>
        </div>
      </header>
      <main className="flex-1 overflow-auto">
        <div className="container mx-auto px-24 grid gap-6 py-10">
          <div className="border rounded-lg shadow-sm p-6 w-full">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead className="w-[150px]">이름</TableHead>
                  <TableHead className="w/[100px]">정당</TableHead>
                  <TableHead className="w/[150px]">지역구</TableHead>
                  <TableHead className="text-right">출석률</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                <MemberTableRow name="홍길동" party="더불어민주당" district="서울 강남구" attendance="95%" />
                <MemberTableRow name="김철수" party="국민의힘" district="부산 해운대구" attendance="92%" />
                <MemberTableRow name="이영희" party="정의당" district="광주 북구" attendance="90%" />
                <MemberTableRow name="박민지" party="더불어민주당" district="대전 유성구" attendance="88%" />
                <MemberTableRow name="최준혁" party="국민의힘" district="인천 남동구" attendance="85%" />
                <MemberTableRow name="김지영" party="정의당" district="경기 수원시" attendance="82%" />
                <MemberTableRow name="이철호" party="더불어민주당" district="울산 중구" attendance="80%" />
                <MemberTableRow name="박영수" party="국민의힘" district="경북 포항시" attendance="78%" />
              </TableBody>
            </Table>
          </div>
        </div>
      </main>
    </>
  );
}

function ArrowUpDownIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m21 16-4 4-4-4" />
      <path d="M17 20V4" />
      <path d="m3 8 4-4 4 4" />
      <path d="M7 4v16" />
    </svg>
  );
}

function ChevronDownIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m6 9 6 6 6-6" />
    </svg>
  );
}

function LocateIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <line x1="2" x2="5" y1="12" y2="12" />
      <line x1="19" x2="22" y1="12" y2="12" />
      <line x1="12" x2="12" y1="2" y2="5" />
      <line x1="12" x2="12" y1="19" y2="22" />
      <circle cx="12" cy="12" r="7" />
    </svg>
  );
}

function MenuIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <line x1="4" x2="20" y1="12" y2="12" />
      <line x1="4" x2="20" y1="6" y2="6" />
      <line x1="4" x2="20" y1="18" y2="18" />
    </svg>
  );
}

function MountainIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m8 3 4 8 5-5 5 15H2L8 3z" />
    </svg>
  );
}

function PartyPopperIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M5.8 11.3 2 22l10.7-3.79" />
      <path d="M4 3h.01" />
      <path d="M22 8h.01" />
      <path d="M15 2h.01" />
      <path d="M22 20h.01" />
      <path d="m22 2-2.24.75a2.9 2.9 0 0 0-1.96 3.12v0c.1.86-.57 1.63-1.45 1.63h-.38c-.86 0-1.6.6-1.76 1.44L14 10" />
      <path d="m22 13-.82-.33c-.86-.34-1.82.2-1.98 1.11v0c-.11.7-.72 1.22-1.43 1.22H17" />
      <path d="m11 2 .33.82c.34.86-.2 1.82-1.11 1.98v0C9.52 4.9 9 5.52 9 6.23V7" />
      <path d="M11 13c1.93 1.93 2.83 4.17 2 5-.83.83-3.07-.07-5-2-1.93-1.93-2.83-4.17-2-5 .83-.83 3.07.07 5 2Z" />
    </svg>
  );
}

function SearchIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="11" cy="11" r="8" />
      <path d="m21 21-4.3-4.3" />
    </svg>
  );
}

function StarIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" />
    </svg>
  );
}

