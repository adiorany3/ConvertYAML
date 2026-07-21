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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=207ms, nekobox=240ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-73MS` (url=202ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=200ms, nekobox=228ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=197ms, nekobox=432ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-102MS` (url=212ms, nekobox=236ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-96MS` (url=264ms, nekobox=234ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-97MS` (url=218ms, nekobox=237ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-75MS` (url=213ms, nekobox=241ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-122MS` (url=225ms, nekobox=246ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS` (url=202ms, nekobox=246ms, status=yes)
11. `AKUN-011-156-239-245-0-156-239-24-VLESS-WS-111MS` (url=202ms, status=HTTP 204)
12. `AKUN-012-WEBEX-VLESS-WS-116MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-91MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-93MS` (url=208ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-96MS` (url=250ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-153MS` (url=244ms, status=HTTP 204)
17. `AKUN-017-ZOOM-VLESS-WS-78MS` (url=209ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-112MS` (url=258ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-166MS` (url=709ms, status=HTTP 204)
20. `AKUN-020-ES-FORNEX-20160629-VLESS-WS-109MS` (url=226ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-171MS` (url=221ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-114MS` (url=200ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-129MS` (url=213ms, status=HTTP 204)
24. `AKUN-024-ZVC-VLESS-WS-110MS` (url=215ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-230MS` (url=497ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
