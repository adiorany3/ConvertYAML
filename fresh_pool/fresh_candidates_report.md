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
1. `AKUN-001-ZVC-VLESS-WS-77MS` (url=244ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=215ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=228ms, nekobox=265ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=226ms, nekobox=252ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-79MS` (url=199ms, nekobox=235ms, status=yes)
6. `AKUN-006-WPENG-VLESS-WS-97MS` (url=210ms, nekobox=248ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-90MS` (url=205ms, nekobox=244ms, status=yes)
8. `AKUN-008-OVH-VLESS-WS-91MS` (url=228ms, nekobox=250ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-95MS` (url=206ms, nekobox=268ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-92MS` (url=204ms, nekobox=259ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-99MS` (url=214ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-95MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-103MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-107MS` (url=227ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-114MS` (url=198ms, status=HTTP 204)
16. `AKUN-016-PUBLICDOMAINREGISTRY-NET-VLESS-WS-123MS` (url=237ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-96MS` (url=261ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-123MS` (url=226ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-131MS` (url=211ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-130MS` (url=251ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-113MS` (url=222ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-241MS` (url=523ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-266MS` (url=571ms, status=HTTP 204)
24. `AKUN-024-SPEEDTEST-VLESS-WS-249MS` (url=544ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-275MS` (url=590ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
