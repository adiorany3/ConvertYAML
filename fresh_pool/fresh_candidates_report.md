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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=226ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-63MS` (url=224ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-69MS` (url=222ms, nekobox=248ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-63MS` (url=244ms, nekobox=263ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-69MS` (url=230ms, nekobox=276ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS` (url=237ms, nekobox=251ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS` (url=239ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS` (url=238ms, nekobox=270ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-79MS` (url=218ms, nekobox=7177ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-78MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-86MS`
12. `AKUN-012-SHOPIFY-VLESS-WS-109MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-72MS` (url=238ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-78MS` (url=227ms, status=HTTP 204)
15. `AKUN-015-008500-VLESS-WS-96MS` (url=231ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-107MS` (url=259ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-83MS` (url=323ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-132MS` (url=228ms, status=HTTP 204)
19. `AKUN-019-ZOOM-VLESS-WS-62MS` (url=300ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-110MS` (url=288ms, status=HTTP 204)
21. `AKUN-021-3666888-VLESS-WS-79MS` (url=242ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-138MS` (url=285ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-110MS` (url=284ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-116MS` (url=284ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-113MS` (url=286ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
