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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-87MS` (url=205ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-91MS` (url=216ms, nekobox=232ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS` (url=203ms, nekobox=235ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-102MS` (url=202ms, nekobox=231ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-98MS` (url=211ms, nekobox=243ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-102MS` (url=209ms, nekobox=239ms, status=yes)
7. `AKUN-007-PUBLICDOMAINREGISTRY-NET-VLESS-WS-107MS` (url=207ms, nekobox=235ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-108MS` (url=208ms, nekobox=234ms, status=yes)
9. `AKUN-009-NET-82-21-84-0-24-VLESS-WS-100MS` (url=205ms, nekobox=268ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS` (url=211ms, nekobox=260ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-115MS` (url=213ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-118MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-108MS` (url=313ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-128MS` (url=234ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-130MS` (url=230ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-96MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-117MS` (url=202ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-104MS` (url=202ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-93MS` (url=206ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-123MS` (url=244ms, status=HTTP 204)
21. `AKUN-021-ORG-VLESS-WS-136MS` (url=245ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-123MS` (url=224ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-125MS` (url=251ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-110MS` (url=234ms, status=HTTP 204)
25. `AKUN-025-ADF-VLESS-WS-116MS` (url=214ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
