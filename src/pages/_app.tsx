import type { AppProps } from 'next/app'
import { ChakraProvider } from '@/components/chakra-provider'
import MyFooter from '@/layout/footer'
import NavHero from '@/layout/header'

export default function App({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider>
      <NavHero />
      <Component {...pageProps} />
      <MyFooter />
    </ChakraProvider>
  )
}
