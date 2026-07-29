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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-ZVC-VLESS-WS-58MS` (url=238ms, nekobox=243ms, status=yes)
2. `AKUN-002-OVH-VLESS-WS-60MS` (url=210ms, nekobox=253ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-55MS` (url=212ms, nekobox=253ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS` (url=212ms, nekobox=249ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-73MS` (url=216ms, nekobox=238ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-58MS` (url=214ms, nekobox=238ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-85MS` (url=209ms, nekobox=255ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-92MS` (url=216ms, nekobox=236ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-107MS` (url=219ms, nekobox=257ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-112MS` (url=202ms, nekobox=236ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-116MS` (url=246ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-96MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-OPENAI-VLESS-WS-109MS` (url=195ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-96MS` (url=234ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-115MS` (url=198ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-80MS` (url=252ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-119MS` (url=248ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-141MS` (url=247ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-132MS` (url=317ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-126MS` (url=238ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-119MS` (url=230ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-161MS` (url=249ms, status=HTTP 204)
23. `AKUN-023-RMGYVPN-VLESS-WS-267MS` (url=622ms, status=HTTP 204)
24. `AKUN-028-ZABIDAT-VLESS-WS-661MS` (url=1092ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-668MS` (url=1155ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
