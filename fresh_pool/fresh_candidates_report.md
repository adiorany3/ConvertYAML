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
1. `AKUN-001-UNKNOWN-VLESS-WS-80MS` (url=293ms, nekobox=361ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=331ms, nekobox=410ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-99MS` (url=311ms, nekobox=359ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-109MS` (url=296ms, nekobox=340ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-114MS` (url=350ms, nekobox=390ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-113MS` (url=329ms, nekobox=367ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-116MS` (url=380ms, nekobox=406ms, status=yes)
8. `AKUN-008-UDACITY-VLESS-WS-102MS` (url=300ms, nekobox=347ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-117MS` (url=416ms, nekobox=403ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-124MS` (url=385ms, nekobox=406ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-118MS` (url=341ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-135MS` (url=297ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-129MS` (url=312ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-143MS` (url=374ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-108MS` (url=395ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-127MS` (url=318ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-147MS` (url=447ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-141MS` (url=359ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-122MS` (url=316ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-106MS` (url=271ms, status=HTTP 204)
21. `AKUN-021-MYBB-VLESS-WS-105MS` (url=352ms, status=HTTP 204)
22. `AKUN-022-US-VLESS-WS-159MS` (url=352ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-139MS` (url=298ms, status=HTTP 204)
24. `AKUN-024-DEV-VLESS-WS-127MS` (url=310ms, status=HTTP 204)
25. `AKUN-025-1PASSWORD-VLESS-WS-150MS` (url=420ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
