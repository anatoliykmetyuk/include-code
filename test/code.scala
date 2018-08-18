import cats._, cats.implicits._, cats.data._, cats.effect._

// start snippet outer
object Main {
  // start snippet inner
  def main(args: Array[String]): Unit = {

    println("Hello World")    

  }
  // end snippet inner
}
// end snippet outer

  // start snippet RichWrappers
  implicit def showExn: Show[Throwable] = Show.show[Throwable] { e =>
    s"${e.getMessage}\n${e.getStackTrace.mkString("\n")}"
  }

  implicit class RichEither[E: Show, A](x: Either[E, A]) {
    def etr: Ef[A] = EitherT.fromEither[IO](x).leftMap(_.show)
  }

  implicit class RichDelayed[A](x: => A) {
    def sus: Ef[A] = EitherT.right[String](IO { x })
    def exn: Ef[A] = Try(x).toEither.etr
  }
  // end snippet RichWrappers
