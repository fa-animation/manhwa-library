import { Container as ContainerChakra } from '@chakra-ui/react'
import { ContainerProps } from '@chakra-ui/layout'

interface ContainerP extends ContainerProps {
  children: React.ReactNode
}

const Container = ({ children, ...rest }: ContainerP) => (
  <ContainerChakra maxW="1280px" {...rest}>
    {children}
  </ContainerChakra>
)

export default Container
