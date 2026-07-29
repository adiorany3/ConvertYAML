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
1. `AKUN-001-UNKNOWN-VLESS-WS-119MS` (url=241ms, nekobox=305ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-121MS` (url=300ms, nekobox=278ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-108MS` (url=276ms, nekobox=324ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-118MS` (url=320ms, nekobox=322ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-115MS` (url=282ms, nekobox=310ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-111MS` (url=251ms, nekobox=308ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-130MS` (url=231ms, nekobox=284ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-123MS` (url=293ms, nekobox=299ms, status=yes)
9. `AKUN-009-SPEEDTEST-VLESS-WS-132MS` (url=259ms, nekobox=210ms, status=no)
10. `AKUN-009-UNKNOWN-VLESS-WS-128MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-133MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-99MS` (url=272ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-114MS` (url=262ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-133MS` (url=267ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-117MS` (url=280ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-134MS` (url=352ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-136MS` (url=252ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-123MS` (url=301ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-156MS` (url=273ms, status=HTTP 204)
20. `AKUN-020-1PASSWORD-VLESS-WS-125MS` (url=270ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-172MS` (url=376ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-230MS` (url=370ms, status=HTTP 204)
23. `AKUN-023-CCWU-VLESS-WS-115MS` (url=263ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-113MS` (url=237ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-278MS` (url=696ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
