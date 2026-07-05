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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=232ms, nekobox=277ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=272ms, nekobox=187ms, status=no)
3. `AKUN-002-ZVC-VLESS-WS-70MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS`
5. `AKUN-004-OVH-VLESS-WS-64MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS`
7. `AKUN-006-INTERNETWORKS-45-131-208-VLESS-WS-84MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-62MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS`
10. `AKUN-009-WPENG-VLESS-WS-69MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-101MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-106MS` (url=242ms, status=HTTP 204)
13. `AKUN-013-466688-VLESS-WS-76MS` (url=248ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-109MS` (url=247ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-87MS` (url=280ms, status=HTTP 204)
16. `AKUN-016-WPENG-VLESS-WS-109MS` (url=242ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-227MS` (url=2534ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-281MS` (url=657ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-267MS` (url=568ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-291MS` (url=856ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-294MS` (url=566ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-297MS` (url=605ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-292MS` (url=593ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-271MS` (url=545ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-463MS` (url=816ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
