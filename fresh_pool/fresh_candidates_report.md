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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-82MS` (url=274ms, nekobox=311ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=277ms, nekobox=311ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=371ms, nekobox=396ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=272ms, nekobox=303ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-99MS` (url=274ms, nekobox=315ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-103MS` (url=365ms, nekobox=410ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-113MS` (url=370ms, nekobox=328ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-114MS` (url=317ms, nekobox=305ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-115MS` (url=288ms, nekobox=310ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-100MS` (url=323ms, nekobox=306ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-103MS` (url=282ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-124MS` (url=626ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=326ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-113MS` (url=370ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-158MS` (url=338ms, status=HTTP 204)
16. `AKUN-016-CCWU-VLESS-WS-141MS` (url=306ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-143MS` (url=298ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-108MS` (url=238ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-151MS` (url=311ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-171MS` (url=307ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-169MS` (url=355ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-193MS` (url=289ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-120MS` (url=589ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-95MS` (url=335ms, status=HTTP 204)
25. `AKUN-025-WEBEX-VLESS-WS-90MS` (url=376ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
