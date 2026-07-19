class LogLineParser
  def initialize(line)
    @line = line
  end

  def message
    return @line[@line.index(":") + 1..].strip
  end

  def log_level
    return @line[1..@line.index("]") - 1].downcase
  end

  def reformat
    return "#{message} (#{log_level})"
  end
end
