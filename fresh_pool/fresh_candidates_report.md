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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-113MS` (url=285ms, nekobox=324ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-121MS` (url=277ms, nekobox=363ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-128MS` (url=287ms, nekobox=345ms, status=yes)
4. `AKUN-004-SAVVY-7-VLESS-WS-122MS` (url=299ms, nekobox=374ms, status=yes)
5. `AKUN-005-466688-VLESS-WS-117MS` (url=322ms, nekobox=361ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-113MS` (url=297ms, nekobox=322ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-118MS` (url=319ms, nekobox=305ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-136MS` (url=362ms, nekobox=347ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-124MS` (url=335ms, nekobox=490ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-138MS` (url=324ms, nekobox=356ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-115MS` (url=300ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-116MS` (url=295ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-105MS` (url=382ms, status=HTTP 204)
14. `AKUN-014-UK-GB-DCL-01-20191003-VLESS-WS-141MS` (url=353ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-144MS` (url=359ms, status=HTTP 204)
16. `AKUN-016-UK-GB-DCL-01-20191003-VLESS-WS-143MS` (url=331ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-157MS` (url=346ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-146MS` (url=364ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-161MS` (url=413ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-149MS` (url=285ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-163MS` (url=348ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-155MS` (url=333ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-167MS` (url=357ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-168MS` (url=300ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-207MS` (url=414ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
