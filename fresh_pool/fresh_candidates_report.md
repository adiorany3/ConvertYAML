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
1. `AKUN-001-090227-VLESS-WS-78MS` (url=272ms, nekobox=263ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-109MS`
3. `AKUN-003-UNKNOWN-VLESS-WS-123MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-118MS`
5. `AKUN-005-UNKNOWN-VLESS-WS-91MS`
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-124MS`
7. `AKUN-008-CLOUDFLARE-VLESS-WS-114MS` (url=261ms, nekobox=187ms, status=no)
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS`
10. `AKUN-009-SPEEDTEST-VLESS-WS-311MS`
11. `AKUN-010-CONFLU-VLESS-WS-339MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-308MS` (url=685ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-326MS` (url=3777ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-344MS` (url=3417ms, status=HTTP 204)
15. `AKUN-016-MICROSOFT-VLESS-WS-345MS` (url=645ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-403MS` (url=1398ms, status=HTTP 204)
17. `AKUN-024-CLOUDFLARE-VLESS-WS-466MS` (url=1310ms, status=HTTP 204)
18. `AKUN-028-CLOUDFLARE-VLESS-WS-510MS` (url=905ms, status=HTTP 204)
19. `AKUN-035-CLOUDFLARE-VLESS-WS-606MS` (url=711ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
