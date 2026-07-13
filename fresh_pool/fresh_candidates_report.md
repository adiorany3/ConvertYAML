# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 30

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-112MS` (url=343ms, nekobox=220ms, status=no)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=308ms, nekobox=5159ms, status=no)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-113MS` (url=274ms, nekobox=231ms, status=no)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-113MS` (url=275ms, nekobox=5153ms, status=no)
5. `AKUN-001-CLOUDFLARE-VLESS-WS-113MS`
6. `AKUN-002-UNKNOWN-VLESS-WS-123MS`
7. `AKUN-003-DEV-VLESS-WS-127MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-127MS` (url=319ms, nekobox=5156ms, status=no)
9. `AKUN-009-DEV-VLESS-WS-125MS` (url=297ms, nekobox=224ms, status=no)
10. `AKUN-004-CLOUDFLARE-VLESS-WS-131MS`
11. `AKUN-011-UNKNOWN-VLESS-WS-121MS` (url=422ms, nekobox=5156ms, status=no)
12. `AKUN-005-UNKNOWN-VLESS-WS-128MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-125MS` (url=348ms, nekobox=5156ms, status=no)
14. `AKUN-006-UNKNOWN-VLESS-WS-128MS`
15. `AKUN-007-UNKNOWN-VLESS-WS-125MS`
16. `AKUN-016-CLOUDFLARE-VLESS-WS-120MS` (url=455ms, nekobox=5155ms, status=no)
17. `AKUN-017-UNKNOWN-VLESS-WS-123MS` (url=277ms, nekobox=5156ms, status=no)
18. `AKUN-008-NODEHOST-VLESS-WS-156MS`
19. `AKUN-009-UNKNOWN-VLESS-WS-141MS`
20. `AKUN-020-ZVC-VLESS-WS-141MS` (url=317ms, nekobox=5156ms, status=no)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-128MS` (url=346ms, nekobox=5157ms, status=no)
22. `AKUN-010-CLOUDFLARE-VLESS-WS-119MS`
23. `AKUN-023-HETZNER-VLESS-WS-152MS` (url=336ms, status=HTTP 204)
24. `AKUN-024-HETZNER-VLESS-WS-165MS` (url=311ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-246MS` (url=690ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
