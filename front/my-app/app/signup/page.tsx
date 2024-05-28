/**
 * v0 by Vercel..
 * @see https://v0.dev/t/cQ9a3KPq9rI
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

export default function Component() {
  return (
    <div className="bg-white min-h-screen">
    <div className="mx-auto max-w-md space-y-6 py-12">
      <div className="space-y-2 text-center">
        <h1 className="text-3xl font-bold">계정 생성</h1>
        <p className="text-gray-500 dark:text-gray-400">아래 단계들을 수행하시오</p>
      </div>
      <form className="space-y-4">
        <div className="space-y-2">
          <Label htmlFor="username">닉네임</Label>
          <Input id="username" placeholder="닉네임을 입력하시오" required />
        </div>
        <div className="space-y-2">
          <Label htmlFor="email">이메일</Label>
          <Input id="email" placeholder="이메일을 입력하시오" required type="email" />
        </div>
        <div className="space-y-2">
          <Label htmlFor="password">비밀번호</Label>
          <Input id="password" placeholder="비밀번호를 입력하시오" required type="password" />
        </div>
        <div className="space-y-2">
          <Label htmlFor="confirm-password">비밀번호 확인</Label>
          <Input id="confirm-password" placeholder="동일한 비밀번호를 다시 입력하시오" required type="password" />
        </div>
        <Button className="w-full" type="submit">
          회원가입
        </Button>
      </form>
    </div>
  </div>
  )
}
