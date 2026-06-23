# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-DIGITALOCEAN-VLESS-WS-76MS` (url=201ms, nekobox=208ms, status=no)
2. `AKUN-001-UNKNOWN-VLESS-WS-83MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS`
4. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-70MS`
5. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-80MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS`
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-108MS`
9. `AKUN-008-BROADNNET-KR-VLESS-WS-124MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-110MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-BROADNNET-KR-VLESS-WS-113MS` (url=243ms, status=HTTP 204)
14. `AKUN-014-CONFLU-VLESS-WS-234MS` (url=494ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-251MS` (url=570ms, status=HTTP 204)
16. `AKUN-016-SPEEDTEST-VLESS-WS-278MS` (url=575ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-256MS` (url=583ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-292MS` (url=546ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-235MS` (url=547ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-243MS` (url=496ms, status=HTTP 204)
21. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-481MS` (url=810ms, status=HTTP 204)
22. `AKUN-029-UNKNOWN-VLESS-WS-471MS` (url=688ms, status=HTTP 204)
23. `AKUN-034-UNKNOWN-VLESS-WS-716MS` (url=2384ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
