# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-UNKNOWN-VLESS-WS-77MS` (url=202ms, nekobox=244ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-84MS` (url=222ms, nekobox=280ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=292ms, nekobox=253ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=203ms, nekobox=260ms, status=yes)
5. `AKUN-005-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-100MS` (url=228ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-74MS` (url=216ms, nekobox=257ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-125MS` (url=227ms, nekobox=206ms, status=no)
8. `AKUN-008-DEV-VLESS-WS-127MS` (url=224ms, nekobox=189ms, status=no)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-130MS` (url=206ms, nekobox=195ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-110MS` (url=242ms, nekobox=228ms, status=no)
11. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS`
12. `AKUN-008-SPEEDTEST-VLESS-WS-243MS`
13. `AKUN-009-CLOUDFLARE-VLESS-WS-277MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-305MS`
15. `AKUN-016-CLOUDFLARE-VLESS-WS-283MS` (url=593ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-285MS` (url=4673ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-280MS` (url=592ms, status=HTTP 204)
18. `AKUN-023-UNKNOWN-VLESS-WS-458MS` (url=718ms, status=HTTP 204)
19. `AKUN-027-UNKNOWN-VLESS-WS-509MS` (url=794ms, status=HTTP 204)
20. `AKUN-030-CLOUDFLARE-VLESS-WS-355MS` (url=622ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
