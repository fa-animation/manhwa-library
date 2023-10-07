import type { DeepPartial, Theme } from '@chakra-ui/react'

export const fonts: DeepPartial<Theme['fonts']> = {
  body: 'Roboto, system-ui, sans-serif',
  heading: 'Roboto, system-ui, sans-serif',
  mono: 'Menlo, monospace'
}

export const fontWeights: DeepPartial<Theme['fontWeights']> = {
  normal: 400,
  medium: 600,
  bold: 700
}

export const fontSizes: DeepPartial<Theme['fontSizes']> = {
  '3xl': '30px',
  '4xl': '38px',
  '5xl': '46px',
  '6xl': '60px'
}
