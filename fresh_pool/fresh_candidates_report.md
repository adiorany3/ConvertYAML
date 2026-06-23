# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 16
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 22

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-130MS` (url=283ms, nekobox=300ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-141MS` (url=273ms, nekobox=302ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-141MS` (url=257ms, nekobox=300ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-149MS` (url=342ms, nekobox=310ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-153MS` (url=308ms, nekobox=307ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-140MS` (url=306ms, nekobox=338ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-362MS`
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-407MS`
9. `AKUN-009-WPENG-VLESS-WS-399MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-376MS`
11. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-418MS` (url=765ms, status=HTTP 204)
12. `AKUN-015-CLOUDFLARE-VLESS-WS-377MS` (url=706ms, status=HTTP 204)
13. `AKUN-017-BROADNNET-KR-VLESS-WS-233MS` (url=318ms, status=HTTP 204)
14. `AKUN-026-CLOUDFLARE-VLESS-WS-371MS` (url=761ms, status=HTTP 204)
15. `AKUN-033-UNKNOWN-VLESS-WS-637MS` (url=945ms, status=HTTP 204)
16. `AKUN-034-UNKNOWN-VLESS-WS-737MS` (url=1837ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
