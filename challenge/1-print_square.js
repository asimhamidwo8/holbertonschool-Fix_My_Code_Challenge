#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  process.exit(1);
}

if (size <= 0) {
  process.exit(0);
}

for (let i = 0; i < size; i++) {
  console.log('#'.repeat(size));
}

