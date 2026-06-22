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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-94MS` (url=294ms, nekobox=262ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-111MS` (url=241ms, nekobox=259ms, status=yes)
3. `AKUN-003-US-VLESS-WS-105MS` (url=218ms, nekobox=252ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-107MS` (url=223ms, nekobox=280ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-101MS` (url=241ms, nekobox=273ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-109MS` (url=227ms, nekobox=259ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-124MS` (url=227ms, nekobox=213ms, status=no)
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-124MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-115MS`
10. `AKUN-009-VULTR-VLESS-WS-107MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-115MS`
12. `AKUN-012-DEV-VLESS-WS-108MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-139MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-112MS` (url=231ms, status=HTTP 204)
15. `AKUN-015-008500-VLESS-WS-129MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-147MS` (url=268ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-104MS` (url=221ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-139MS` (url=252ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-139MS` (url=223ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-121MS` (url=248ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-207MS` (url=257ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-154MS` (url=231ms, status=HTTP 204)
23. `AKUN-023-BROADNNET-KR-VLESS-WS-103MS` (url=223ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-394MS` (url=789ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-404MS` (url=820ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
