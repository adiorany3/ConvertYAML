# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 19
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 25

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=223ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=221ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-96MS` (url=226ms, nekobox=260ms, status=no)
4. `AKUN-003-UNKNOWN-VLESS-WS-72MS`
5. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-113MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-92MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-256MS`
12. `AKUN-013-VERCEL-VLESS-WS-275MS` (url=2489ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-263MS` (url=550ms, status=HTTP 204)
14. `AKUN-016-UNKNOWN-VLESS-WS-306MS` (url=625ms, status=HTTP 204)
15. `AKUN-018-UNKNOWN-VLESS-WS-429MS` (url=1529ms, status=HTTP 204)
16. `AKUN-019-JISON-VLESS-WS-348MS` (url=646ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-293MS` (url=561ms, status=HTTP 204)
18. `AKUN-032-CLOUDFLARE-VLESS-WS-265MS` (url=538ms, status=HTTP 204)
19. `AKUN-035-UNKNOWN-VLESS-WS-617MS` (url=1046ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
