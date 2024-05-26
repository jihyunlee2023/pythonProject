/**
 * v0 by Vercel.
 * @see https://v0.dev/t/cbxrIiibG0u
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { CardContent, CardFooter, Card } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import Link from "next/link"

export default function Component() {
  return (
    <div className="flex h-screen w-full items-center justify-center bg-gray-100 dark:bg-gray-950">
      <div className="mx-auto max-w-[400px] w-full space-y-6">
        <div className="flex flex-col items-center space-y-2">
          <MountainIcon className="h-10 w-10" />
          <h1 className="text-2xl font-bold">Welcome back</h1>
        </div>
        <Card>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="email">Email</Label>
              <Input id="email" placeholder="m@example.com" required type="email" />
            </div>
            <div className="space-y-2">
              <Label htmlFor="password">Password</Label>
              <Input id="password" required type="password" />
            </div>
          </CardContent>
          <CardFooter>
            <Button className="w-full">Sign in</Button>
          </CardFooter>
        </Card>
        <div className="text-center text-sm text-gray-500 dark:text-gray-400">
          Don't have an account?
          <Link className="font-medium underline underline-offset-4" href="signup">
            Sign up
          </Link>
        </div>
      </div>
    </div>
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