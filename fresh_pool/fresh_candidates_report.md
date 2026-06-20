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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-90MS` (url=203ms, nekobox=260ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-101MS` (url=219ms, nekobox=367ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-103MS` (url=212ms, nekobox=210ms, status=no)
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-99MS`
5. `AKUN-004-VULTR-VLESS-WS-95MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-102MS` (url=211ms, nekobox=200ms, status=no)
7. `AKUN-005-CLOUDFLARE-VLESS-WS-100MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS` (url=226ms, nekobox=201ms, status=no)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=211ms, nekobox=200ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-130MS` (url=209ms, nekobox=199ms, status=no)
11. `AKUN-006-CLOUDFLARE-VLESS-WS-116MS`
12. `AKUN-007-CLOUDFLARE-VLESS-WS-111MS`
13. `AKUN-008-BROADNNET-KR-VLESS-WS-94MS`
14. `AKUN-009-UNKNOWN-VLESS-WS-368MS`
15. `AKUN-010-CLOUDFLARE-VLESS-WS-392MS`
16. `AKUN-016-UNKNOWN-VLESS-WS-398MS` (url=853ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-407MS` (url=811ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-412MS` (url=815ms, status=HTTP 204)
19. `AKUN-026-UNKNOWN-VLESS-WS-693MS` (url=1091ms, status=HTTP 204)
20. `AKUN-027-UNKNOWN-VLESS-WS-702MS` (url=1158ms, status=HTTP 204)
21. `AKUN-029-UNKNOWN-VLESS-WS-751MS` (url=1220ms, status=HTTP 204)
22. `AKUN-032-UNKNOWN-VLESS-WS-823MS` (url=1192ms, status=HTTP 204)
23. `AKUN-033-UNKNOWN-VLESS-WS-777MS` (url=1302ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-869MS` (url=3298ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-857MS` (url=1453ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
