import {
  Accordion,
  AccordionButton,
  AccordionIcon,
  AccordionItem,
  AccordionPanel,
  Box,
  Button,
  Card,
  CardBody,
  CardFooter,
  Heading,
  Image,
  Stack,
  Text
} from '@chakra-ui/react'

type IChapter = {
  title: string;
  description: string
}

export const Chapter = ({title,description}:IChapter) => {
  return (
    <>
      <AccordionItem>
        <h2>
          <AccordionButton>
            <Box as="span" flex="1" textAlign="left">
              {title}
            </Box>
            <AccordionIcon />
          </AccordionButton>
        </h2>
        <AccordionPanel pb={4}>
          <Card direction={{ base: 'column', sm: 'row' }} overflow="hidden" variant="outline">
              <CardBody>
                <Heading size="md">The perfect latte</Heading>
                <Text py="2">
                  {description}
                </Text>
              </CardBody>
              <CardFooter>
                <Button variant="solid" colorScheme="blue">
                  Buy Latte
                </Button>
              </CardFooter>
          </Card>
        </AccordionPanel>
      </AccordionItem>
    </>
  )
}
