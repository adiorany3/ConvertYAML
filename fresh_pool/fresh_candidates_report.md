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
1. `AKUN-001-NEXUSMODS-VLESS-WS-86MS` (url=205ms, nekobox=236ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-93MS` (url=208ms, nekobox=231ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS` (url=212ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=267ms, nekobox=236ms, status=yes)
5. `AKUN-005-466688-VLESS-WS-91MS` (url=221ms, nekobox=271ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-106MS` (url=240ms, nekobox=258ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=213ms, nekobox=238ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS` (url=221ms, nekobox=246ms, status=yes)
9. `AKUN-009-GO-DADDY-COM-LLC-VLESS-WS-119MS` (url=210ms, nekobox=246ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-125MS` (url=212ms, nekobox=242ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-128MS` (url=244ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-130MS` (url=209ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-119MS` (url=237ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-127MS` (url=210ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-129MS` (url=253ms, status=HTTP 204)
16. `AKUN-016-UK-GB-DCL-01-20191003-VLESS-WS-142MS` (url=249ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-134MS` (url=262ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-148MS` (url=272ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-115MS` (url=224ms, status=HTTP 204)
20. `AKUN-020-WPENG-VLESS-WS-102MS` (url=222ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-124MS` (url=220ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-147MS` (url=232ms, status=HTTP 204)
23. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-152MS` (url=698ms, status=HTTP 204)
24. `AKUN-024-POLICE-VLESS-WS-153MS` (url=237ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-178MS` (url=223ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
