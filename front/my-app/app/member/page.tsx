/**
 * v0 by Vercel.
 * @see https://v0.dev/t/LSIn0jTQR2v
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
import { CollapsibleTrigger, CollapsibleContent, Collapsible } from "@/components/ui/collapsible"
import Link from "next/link"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { DropdownMenuTrigger, DropdownMenuRadioItem, DropdownMenuRadioGroup, DropdownMenuContent, DropdownMenu } from "@/components/ui/dropdown-menu"
import { AvatarImage, AvatarFallback, Avatar } from "@/components/ui/avatar"

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
              className="pl-8 sm:w-[300px] md:w-[200px] lg:w-[300px] bg-gray-800 text-gray-50 placeholder:text-gray-400"
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
          <Button className="bg-gray-800 text-gray-50 hover:bg-gray-700" variant="outline">
            로그인
          </Button>
        </div>
      </header>
      <main className="flex-1 overflow-auto">
        <div className="container mx-auto px-24 grid gap-6 py-10">
          <div className="border rounded-lg shadow-sm p-6 w-full">
            <div className="grid grid-cols-3 gap-6">
              <div className="col-span-2">
                <div className="space-y-6">
                  <div>
                    <h2 className="text-2xl font-bold">홍길동 의원</h2>
                    <div className="flex items-center gap-2 text-gray-500 dark:text-gray-400">
                      <PartyPopperIcon className="w-5 h-5" />
                      <span>더불어민주당</span>
                      <LocateIcon className="w-5 h-5" />
                      <span>서울 강남구</span>
                    </div>
                  </div>
                  <div>
                    <h3 className="text-lg font-bold">신상정보</h3>
                    <div className="grid grid-cols-2 gap-4 text-sm text-gray-500 dark:text-gray-400">
                      <div>
                        <span className="font-medium">생년월일:</span>
                        1970년 5월 1일
                      </div>
                      <div>
                        <span className="font-medium">학력:</span>
                        서울대학교 정치학과 졸업
                      </div>
                      <div>
                        <span className="font-medium">경력:</span>
                        국회의원 3선, 국회 행정안전위원회 위원장
                      </div>
                      <div>
                        <span className="font-medium">주요 법안:</span>
                        지방자치법 개정안, 정보공개법 개정안
                      </div>
                    </div>
                  </div>
                  <div>
                    <h3 className="text-lg font-bold">국회활동</h3>
                    <div className="grid grid-cols-2 gap-4 text-sm text-gray-500 dark:text-gray-400">
                      <div>
                        <span className="font-medium">출석률:</span>
                        95%
                      </div>
                      <div>
                        <span className="font-medium">발언 횟수:</span>
                        120회
                      </div>
                      <div>
                        <span className="font-medium">대표 발의 법안:</span>
                        지방자치법 개정안, 정보공개법 개정안
                      </div>
                      <div>
                        <span className="font-medium">위원회 활동:</span>
                        행정안전위원회 위원장
                      </div>
                    </div>
                  </div>
                  <div>
                    <h3 className="text-lg font-bold">최근 뉴스</h3>
                    <div className="grid grid-cols-1 gap-4">
                      <div className="border rounded-lg shadow-sm p-4">
                        <h4 className="text-base font-bold">홍길동 의원, 지방자치법 개정안 발의</h4>
                        <p className="text-sm text-gray-500 dark:text-gray-400">
                          홍길동 의원은 지방자치단체의 자치권 강화를 위한 지방자치법 개정안을 대표 발의했습니다. 이
                          법안은 지방정부의 자율성을 높이고 주민 참여를 확대하는 것을 주요 내용으로 하고 있습니다.
                        </p>
                        <div className="flex justify-end text-sm text-gray-500 dark:text-gray-400">2023년 4월 15일</div>
                      </div>
                      <div className="border rounded-lg shadow-sm p-4">
                        <h4 className="text-base font-bold">홍길동 의원, 정보공개법 개정안 발의</h4>
                        <p className="text-sm text-gray-500 dark:text-gray-400">
                          홍길동 의원은 정부 정보의 투명성 제고를 위한 정보공개법 개정안을 대표 발의했습니다. 이 법안은
                          국민의 알권리 보장과 행정의 책임성 강화를 목적으로 하고 있습니다.
                        </p>
                        <div className="flex justify-end text-sm text-gray-500 dark:text-gray-400" />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
      <div className="container mx-auto px-24 grid gap-6 py-10">
        <div className="border rounded-lg shadow-sm p-6 w-full">
          <div className="grid grid-cols-3 gap-6">
            <div className="col-span-2">
              <div className="space-y-6">
                <div>
                  <h2 className="text-2xl font-bold">홍길동 의원</h2>
                  <div className="flex items-center gap-2 text-gray-500 dark:text-gray-400">
                    <PartyPopperIcon className="w-5 h-5" />
                    <span>더불어민주당</span>
                    <LocateIcon className="w-5 h-5" />
                    <span>서울 강남구</span>
                  </div>
                </div>
                <div>
                  <h3 className="text-lg font-bold">신상정보</h3>
                  <div className="grid grid-cols-2 gap-4 text-sm text-gray-500 dark:text-gray-400">
                    <div>
                      <span className="font-medium">생년월일:</span>
                      1970년 5월 1일
                    </div>
                    <div>
                      <span className="font-medium">학력:</span>
                      서울대학교 정치학과 졸업
                    </div>
                    <div>
                      <span className="font-medium">경력:</span>
                      국회의원 3선, 국회 행정안전위원회 위원장
                    </div>
                    <div>
                      <span className="font-medium">주요 법안:</span>
                      지방자치법 개정안, 정보공개법 개정안
                    </div>
                  </div>
                </div>
                <div>
                  <h3 className="text-lg font-bold">국회활동</h3>
                  <div className="grid grid-cols-2 gap-4 text-sm text-gray-500 dark:text-gray-400">
                    <div>
                      <span className="font-medium">출석률:</span>
                      95%
                    </div>
                    <div>
                      <span className="font-medium">발언 횟수:</span>
                      120회
                    </div>
                    <div>
                      <span className="font-medium">대표 발의 법안:</span>
                      지방자치법 개정안, 정보공개법 개정안
                    </div>
                    <div>
                      <span className="font-medium">위원회 활동:</span>
                      행정안전위원회 위원장
                    </div>
                  </div>
                </div>
                <div>
                  <h3 className="text-lg font-bold">최근 뉴스</h3>
                  <div className="grid grid-cols-1 gap-4">
                    <div className="border rounded-lg shadow-sm p-4">
                      <h4 className="text-base font-bold">홍길동 의원, 지방자치법 개정안 발의</h4>
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        홍길동 의원은 지방자치단체의 자치권 강화를 위한 지방자치법 개정안을 대표 발의했습니다. 이 법안은
                        지방정부의 자율성을 높이고 주민 참여를 확대하는 것을 주요 내용으로 하고 있습니다.
                      </p>
                      <div className="flex justify-end text-sm text-gray-500 dark:text-gray-400">2023년 4월 15일</div>
                    </div>
                    <div className="border rounded-lg shadow-sm p-4">
                      <h4 className="text-base font-bold">홍길동 의원, 정보공개법 개정안 발의</h4>
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        홍길동 의원은 정부 정보의 투명성 제고를 위한 정보공개법 개정안을 대표 발의했습니다. 이 법안은
                        국민의 알권리 보장과 행정의 책임성 강화를 목적으로 하고 있습니다.
                      </p>
                      <div className="flex justify-end text-sm text-gray-500 dark:text-gray-400" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  )
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
  )
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
  )
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
  )
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
  )
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
  )
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
  )
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
  )
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
  )
}