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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=227ms, nekobox=190ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-90MS` (url=228ms, nekobox=195ms, status=no)
5. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS`
6. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS`
7. `AKUN-005-VULTR-VLESS-WS-81MS`
8. `AKUN-006-DIGITALOCEAN-VLESS-WS-70MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-99MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-89MS`
11. `AKUN-009-ADF-VLESS-WS-102MS`
12. `AKUN-010-UNKNOWN-VLESS-WS-81MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-138MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-88MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-US-VLESS-WS-96MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-164MS` (url=210ms, status=HTTP 204)
17. `AKUN-017-OPENAI-VLESS-WS-147MS` (url=215ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-77MS` (url=208ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-246MS` (url=551ms, status=HTTP 204)
20. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-82MS` (url=211ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-258MS` (url=493ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-260MS` (url=556ms, status=HTTP 204)
23. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-262MS` (url=544ms, status=HTTP 204)
24. `AKUN-024-MICROSOFT-VLESS-WS-280MS` (url=570ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-85MS` (url=217ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
