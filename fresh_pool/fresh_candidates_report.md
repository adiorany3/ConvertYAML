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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-73MS` (url=353ms, nekobox=419ms, status=yes)
2. `AKUN-002-ICOOK-VLESS-WS-76MS` (url=334ms, nekobox=395ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-81MS` (url=342ms, nekobox=400ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=279ms, nekobox=309ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=320ms, nekobox=375ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=290ms, nekobox=222ms, status=no)
7. `AKUN-006-FMN5-RENTED-NET2-VLESS-WS-99MS`
8. `AKUN-007-008500-VLESS-WS-94MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-107MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-101MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-90MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-123MS` (url=343ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-85MS` (url=373ms, status=HTTP 204)
14. `AKUN-015-CCWU-VLESS-WS-138MS` (url=312ms, status=HTTP 204)
15. `AKUN-016-LEVIKOGJGFDD-VLESS-WS-101MS` (url=365ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-139MS` (url=296ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-149MS` (url=355ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-92MS` (url=270ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-112MS` (url=373ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-103MS` (url=406ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-194MS` (url=398ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-214MS` (url=304ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-331MS` (url=849ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-593MS` (url=2884ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-589MS` (url=1001ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
