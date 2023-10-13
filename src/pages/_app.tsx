import type { AppProps } from 'next/app'
import { ChakraProvider } from '@/components/chakra-provider'
import MyFooter from '@/layout/footer'

export default function App({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider>
      <Component {...pageProps} />
      <MyFooter />
    </ChakraProvider>
  )
}
