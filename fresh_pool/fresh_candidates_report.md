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
1. `AKUN-001-ZVC-VLESS-WS-61MS` (url=222ms, nekobox=231ms, status=yes)
2. `AKUN-002-PUBLICDOMAINREGISTRY-NET-VLESS-WS-62MS` (url=218ms, nekobox=225ms, status=yes)
3. `AKUN-003-090227-VLESS-WS-66MS` (url=202ms, nekobox=254ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-61MS` (url=206ms, nekobox=227ms, status=yes)
5. `AKUN-005-466688-VLESS-WS-72MS` (url=217ms, nekobox=249ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-77MS` (url=200ms, nekobox=255ms, status=yes)
7. `AKUN-007-877774-VLESS-WS-83MS` (url=209ms, nekobox=254ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-69MS` (url=222ms, nekobox=263ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-87MS` (url=204ms, nekobox=237ms, status=yes)
10. `AKUN-010-HGC-GLOBAL-COMMUNICATION-VLESS-WS-89MS` (url=225ms, nekobox=241ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-88MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-77MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-98MS` (url=201ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-98MS` (url=219ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-103MS` (url=207ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-111MS` (url=211ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-149MS` (url=228ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-81MS` (url=218ms, status=HTTP 204)
19. `AKUN-020-US-VLESS-WS-92MS` (url=215ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-228MS` (url=497ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-236MS` (url=514ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-251MS` (url=551ms, status=HTTP 204)
23. `AKUN-024-QZZ-VLESS-WS-188MS` (url=469ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-241MS` (url=530ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-232MS` (url=333ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
