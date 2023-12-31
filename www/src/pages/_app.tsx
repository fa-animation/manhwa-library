import type { AppProps } from 'next/app'
import { ChakraProvider } from '@/components/chakra-provider'
import MyFooter from '@/layout/footer'
import NavHero from '@/layout/header'
import ProgressBard from '@/components/progressbar'
import FloatingActionButton from '@/components/floating-button'

export default function App({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider>
      <ProgressBard />
      <NavHero />
      <Component {...pageProps} />
      <FloatingActionButton />
      <MyFooter />
    </ChakraProvider>
  )
}
