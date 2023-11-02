import NextNprogress from 'nextjs-progressbar'

const ProgressBard = () => {
  return (
    <NextNprogress
      color="#fb5607"
      startPosition={0.3}
      stopDelayMs={0}
      height={5}
      showOnShallow={true}
      options={{ easing: 'ease', speed: 400 }}
    />
  )
}

export default ProgressBard
