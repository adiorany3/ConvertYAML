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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-73MS` (url=266ms, nekobox=252ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-80MS` (url=227ms, nekobox=253ms, status=yes)
3. `AKUN-003-VULTR-VLESS-WS-81MS` (url=204ms, nekobox=240ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-93MS` (url=206ms, nekobox=260ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-96MS` (url=209ms, nekobox=246ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-92MS` (url=209ms, nekobox=245ms, status=yes)
7. `AKUN-007-466688-VLESS-WS-103MS` (url=208ms, nekobox=247ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-98MS` (url=212ms, nekobox=247ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-104MS` (url=223ms, nekobox=229ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS` (url=204ms, nekobox=7178ms, status=no)
11. `AKUN-010-ZVC-VLESS-WS-91MS`
12. `AKUN-012-UDACITY-VLESS-WS-105MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-98MS` (url=230ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-107MS` (url=203ms, status=HTTP 204)
15. `AKUN-016-POLICE-VLESS-WS-119MS` (url=224ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-128MS` (url=215ms, status=HTTP 204)
17. `AKUN-018-NOTION-WEB-VLESS-WS-117MS` (url=299ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-109MS` (url=229ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-111MS` (url=291ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-110MS` (url=207ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-124MS` (url=214ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-136MS` (url=258ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-101MS` (url=255ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-153MS` (url=217ms, status=HTTP 204)
25. `AKUN-026-POLICE-VLESS-WS-168MS` (url=260ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
