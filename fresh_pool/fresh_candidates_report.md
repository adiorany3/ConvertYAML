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
1. `AKUN-001-UNKNOWN-VLESS-WS-62MS` (url=206ms, nekobox=228ms, status=yes)
2. `AKUN-002-OVH-VLESS-WS-58MS` (url=205ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=198ms, nekobox=226ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-73MS` (url=203ms, nekobox=236ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-71MS` (url=203ms, nekobox=229ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=212ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS` (url=197ms, nekobox=233ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-73MS` (url=204ms, nekobox=245ms, status=yes)
9. `AKUN-009-WTO-VLESS-WS-98MS` (url=225ms, nekobox=224ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-91MS` (url=219ms, nekobox=251ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-103MS` (url=206ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-80MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-78MS` (url=203ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-83MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-90MS` (url=205ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-92MS` (url=217ms, status=HTTP 204)
17. `AKUN-017-ES-FORNEX-20160629-VLESS-WS-116MS` (url=203ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-114MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-102MS` (url=209ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-73MS` (url=220ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-69MS` (url=227ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-107MS` (url=222ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-144MS` (url=198ms, status=HTTP 204)
24. `AKUN-024-CHATGPT-VLESS-WS-82MS` (url=203ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-95MS` (url=217ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
