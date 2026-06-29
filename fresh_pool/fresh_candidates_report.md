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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=230ms, nekobox=227ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-83MS` (url=232ms, nekobox=255ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS` (url=227ms, nekobox=253ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=210ms, nekobox=258ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-100MS` (url=249ms, nekobox=253ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-95MS` (url=223ms, nekobox=251ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-96MS` (url=226ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=199ms, nekobox=200ms, status=no)
9. `AKUN-008-US-VLESS-WS-84MS`
10. `AKUN-009-AEZA-NETWORK-VLESS-WS-96MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-134MS`
12. `AKUN-012-ZVC-VLESS-WS-102MS` (url=257ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-105MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-132MS` (url=202ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-244MS` (url=504ms, status=HTTP 204)
16. `AKUN-017-CONFLU-VLESS-WS-250MS` (url=518ms, status=HTTP 204)
17. `AKUN-018-WPENG-VLESS-WS-277MS` (url=588ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-276MS` (url=592ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-293MS` (url=597ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-279MS` (url=508ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-290MS` (url=640ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-297MS` (url=597ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-319MS` (url=491ms, status=HTTP 204)
24. `AKUN-028-RS-RAPIDSEEDBOX-20190717-VLESS-WS-520MS` (url=852ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-495MS` (url=827ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
