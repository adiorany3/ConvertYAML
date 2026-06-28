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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=217ms, nekobox=252ms, status=yes)
2. `AKUN-002-COMPREND-NET-VLESS-WS-87MS` (url=218ms, nekobox=247ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-94MS` (url=213ms, nekobox=262ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-70MS` (url=228ms, nekobox=248ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-104MS` (url=226ms, nekobox=237ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-102MS` (url=227ms, nekobox=257ms, status=yes)
7. `AKUN-007-466688-VLESS-WS-111MS` (url=231ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS` (url=224ms, nekobox=228ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-94MS` (url=230ms, nekobox=234ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-114MS` (url=216ms, nekobox=223ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-130MS` (url=206ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-119MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-111MS` (url=200ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-75MS` (url=207ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-96MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-229MS` (url=513ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-243MS` (url=500ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-269MS` (url=592ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-266MS` (url=603ms, status=HTTP 204)
20. `AKUN-020-UK-GB-DCL-01-20191003-VLESS-WS-87MS` (url=221ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-293MS` (url=615ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-309MS` (url=556ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-242MS` (url=501ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-280MS` (url=576ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-278MS` (url=570ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
