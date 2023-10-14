import { Heading as ChakraHeading, Text as ChakraText } from '@chakra-ui/react'
import { HeadingProps, TextProps } from '@chakra-ui/layout'

interface PropsHeading extends HeadingProps {
  children: React.ReactNode
}

interface PropsText extends TextProps {
  children: React.ReactNode
}

export const Heading = ({ children, ...props }: PropsHeading) => (
  <ChakraHeading
    as="h3"
    size="md"
    fontWeight="semibold"
    mt="1em"
    mb="0.5em"
    textAlign={'center'}
    {...props}
  >
    {children}
  </ChakraHeading>
)

export const Text = ({ children, ...props }: PropsText) => (
  <ChakraText fontSize="lg" opacity={0.7} {...props} textAlign={'center'}>
    {children}
  </ChakraText>
)
