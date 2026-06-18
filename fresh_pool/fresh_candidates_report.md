# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 11
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 17

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-76MS` (url=232ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=248ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-95MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-342MS`
5. `AKUN-005-UNKNOWN-VLESS-WS-372MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-365MS`
7. `AKUN-007-UNKNOWN-VLESS-WS-391MS`
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-410MS`
9. `AKUN-009-SPEEDTEST-VLESS-WS-376MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-389MS`
11. `AKUN-024-UNKNOWN-VLESS-WS-720MS` (url=1176ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
