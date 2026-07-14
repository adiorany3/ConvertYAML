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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=198ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=204ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=215ms, nekobox=236ms, status=yes)
4. `AKUN-004-IONOS-VLESS-WS-64MS` (url=227ms, nekobox=233ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=193ms, nekobox=246ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-66MS` (url=195ms, nekobox=253ms, status=yes)
7. `AKUN-007-ES-FORNEX-20160629-VLESS-WS-75MS` (url=225ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-92MS` (url=208ms, nekobox=231ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-83MS` (url=224ms, nekobox=251ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-85MS` (url=207ms, nekobox=245ms, status=yes)
11. `AKUN-011-US-VLESS-WS-110MS` (url=225ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-118MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-85MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-88MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-110MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-76MS` (url=197ms, status=HTTP 204)
17. `AKUN-017-PUBLICDOMAINREGISTRY-NET-VLESS-WS-131MS` (url=229ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-74MS` (url=222ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-106MS` (url=218ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-155MS` (url=224ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-115MS` (url=230ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-241MS` (url=321ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-262MS` (url=562ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-231MS` (url=515ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-239MS` (url=2655ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
