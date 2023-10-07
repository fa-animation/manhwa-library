import type { AppProps } from 'next/app'
import { ChakraProvider } from '@/components/chakra-provider'

export default function App({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider>
      <Component {...pageProps} />
    </ChakraProvider>
  )
}
