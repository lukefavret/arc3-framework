# render.py
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

def render(schema_path: Path, tpl_dir: Path, tpl_name: str, out_path: Path):
    data = yaml.safe_load(schema_path.read_text(encoding="utf-8"))
    env = Environment(
        loader=FileSystemLoader(str(tpl_dir)),
        undefined=StrictUndefined,
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    tpl = env.get_template(tpl_name)
    out = tpl.render(**data)
    out_path.write_text(out, encoding="utf-8")
    print("Wrote", out_path)

if __name__ == "__main__":
    schema = Path("./schema/cases/template.yaml")
    tpl_dir = Path("./templates/jinja")
    render(schema, tpl_dir, "obsidian.md.j2", Path("arc3_obsidian.md"))
    render(schema, tpl_dir, "universal.md.j2", Path("arc3_universal.md"))
