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
1. `AKUN-001-UNKNOWN-VLESS-WS-63MS` (url=202ms, nekobox=233ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-68MS` (url=199ms, nekobox=240ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-80MS` (url=202ms, nekobox=249ms, status=yes)
4. `AKUN-004-COMPREND-NET-VLESS-WS-96MS` (url=201ms, nekobox=247ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-94MS` (url=214ms, nekobox=255ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=202ms, nekobox=244ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS` (url=211ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=202ms, nekobox=242ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS` (url=202ms, nekobox=228ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-106MS` (url=209ms, nekobox=246ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-99MS` (url=201ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-108MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-66MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-114MS` (url=200ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-83MS` (url=210ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-236MS` (url=491ms, status=HTTP 204)
17. `AKUN-020-CONFLU-VLESS-WS-245MS` (url=498ms, status=HTTP 204)
18. `AKUN-021-UNKNOWN-VLESS-WS-254MS` (url=544ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-245MS` (url=555ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-225MS` (url=864ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-258MS` (url=550ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-262MS` (url=552ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-78MS` (url=207ms, status=HTTP 204)
24. `AKUN-028-UNKNOWN-VLESS-WS-436MS` (url=803ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-176MS` (url=790ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
