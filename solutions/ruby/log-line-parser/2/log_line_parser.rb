class LogLineParser
  def initialize(line)
    @line = line
    @message = @line[@line.index(":") + 1..].strip
    @log_level = @line[1..@line.index("]") - 1].downcase
  end

  def message
    return @message
  end

  def log_level
    return @log_level
  end

  def reformat
    return "#{message} (#{log_level})"
  end
end
