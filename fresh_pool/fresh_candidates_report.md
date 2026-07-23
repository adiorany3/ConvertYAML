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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-91MS` (url=221ms, nekobox=278ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=206ms, nekobox=251ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS` (url=274ms, nekobox=235ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-90MS` (url=234ms, nekobox=277ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=210ms, nekobox=263ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS` (url=213ms, nekobox=243ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-96MS` (url=230ms, nekobox=259ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-97MS` (url=218ms, nekobox=240ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-95MS` (url=212ms, nekobox=244ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-111MS` (url=239ms, nekobox=208ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-103MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-113MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-112MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-106MS` (url=213ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-118MS` (url=213ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-107MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-135MS` (url=237ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-111MS` (url=215ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-118MS` (url=221ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-140MS` (url=285ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-130MS` (url=206ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-142MS` (url=253ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-140MS` (url=222ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-141MS` (url=246ms, status=HTTP 204)
25. `AKUN-025-ZOOM-VLESS-WS-106MS` (url=211ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
